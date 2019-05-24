package main

import "C"
import (
	"github.com/Azure/azure-extension-foundation/internal/status"
	"github.com/Azure/azure-extension-foundation/sequence"
	"github.com/Azure/azure-extension-foundation/errorhelper"
	"github.com/Azure/azure-extension-foundation/settings"
	"fmt"
)

type ExtensionStatus string

const (
	statusTransitioning ExtensionStatus = "transitioning"
	statusError         ExtensionStatus = "error"
	statusSuccess       ExtensionStatus = "success"
)

// extension specific PublicSettings
type PublicSettings struct {
	Script   string   `json:"script"`
	FileURLs []string `json:"fileUris"`
}

// extension specific ProtectedSettings
type ProtectedSettings struct {
	SecretString       string   `json:"secretString"`
	SecretScript       string   `json:"secretScript"`
	FileURLs           []string `json:"fileUris"`
	StorageAccountName string   `json:"storageAccountName"`
	StorageAccountKey  string   `json:"storageAccountKey"`
}

func (status ExtensionStatus) String() string {
	return string(status)
}

// ReportTransitioning reports the extension status as "transitioning"
//export ReportTransitioning
func ReportTransitioning(operation string, message string) error {
	_, environmentMrseq, err := sequence.GetMostRecentSequenceNumber()
	if err != nil {
		return errorhelper.AddStackToError(fmt.Errorf("unable to get sequence number : %v", err))
	}
	return status.ReportStatus(environmentMrseq, statusTransitioning.String(), operation, message)
}

// ReportError reports the extension status as "error"
//export ReportError
func ReportError(operation string, message string) error {
	_, environmentMrseq, err := sequence.GetMostRecentSequenceNumber()
	if err != nil {
		return errorhelper.AddStackToError(fmt.Errorf("unable to get sequence number : %v", err))
	}
	return status.ReportStatus(environmentMrseq, statusError.String(), operation, message)
}

// ReportSuccess reports the extension status as "success"
//export ReportSuccess
func ReportSuccess(operation string, message string) error {
	_, environmentMrseq, err := sequence.GetMostRecentSequenceNumber()
	if err != nil {
		return errorhelper.AddStackToError(fmt.Errorf("unable to get sequence number : %v", err))
	}
	return status.ReportStatus(environmentMrseq, statusSuccess.String(), operation, message)
}

// UpdateSeqNum updates the sequence number to the most recent sequence number as long as it hasn't been processed
//export UpdateSeqNum
func UpdateSeqNum() error {
	extensionMrseq, environmentMrseq, err := sequence.GetMostRecentSequenceNumber()
	shouldRun := sequence.ShouldBeProcessed(extensionMrseq, environmentMrseq)
	if !shouldRun {
		return errorhelper.AddStackToError(fmt.Errorf("environment mrseq has already been processed by extension (environment mrseq : %v, extension mrseq : %v)\n", environmentMrseq, extensionMrseq))
	}
	err = sequence.SetExtensionMostRecentSequenceNumber(environmentMrseq)
	return err
}

//export GetPublicSettings
func GetPublicSettings() (string, []string) {
	_, environmentMrseq, err := sequence.GetMostRecentSequenceNumber()
	if err != nil {
		errorhelper.AddStackToError(fmt.Errorf("unable to get sequence number: %v", err))
	}

	var publicSettings PublicSettings
	var protectedSettings ProtectedSettings

	err = settings.GetExtensionSettings(environmentMrseq, &publicSettings, &protectedSettings)
	if err != nil {
		errorhelper.AddStackToError(fmt.Errorf("unable to get public settings: %v", err))
	}
	return publicSettings.Script, publicSettings.FileURLs
}

//export GetProtectedSettings
func GetProtectedSettings() (string, string, []string, string, string) {
	_, environmentMrseq, err := sequence.GetMostRecentSequenceNumber()
	if err != nil {
		errorhelper.AddStackToError(fmt.Errorf("unable to get sequence number: %v", err))
	}

	var publicSettings PublicSettings
	var protectedSettings ProtectedSettings

	err = settings.GetExtensionSettings(environmentMrseq, &publicSettings, &protectedSettings)
	if err != nil {
		errorhelper.AddStackToError(fmt.Errorf("unable to get protected settings: %v", err))
	}

	return protectedSettings.SecretString, protectedSettings.SecretScript, protectedSettings.FileURLs, protectedSettings.StorageAccountName, protectedSettings.StorageAccountKey
}

func main(){
}