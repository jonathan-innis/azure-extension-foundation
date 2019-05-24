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

type PublicSettings interface{}
type ProtectedSettings interface{}

func (status ExtensionStatus) String() string {
	return string(status)
}

// ReportTransitioning reports the extension status as "transitioning"
//export ReportTransitioning
func ReportTransitioning(operation string, message string) error {
	_, _, err := sequence.GetMostRecentSequenceNumber()
	if err != nil {
		return errorhelper.AddStackToError(fmt.Errorf("unable to get sequence number : %v", err))
	}
	return nil
	//return status.ReportStatus(environmentMrseq, statusTransitioning.String(), operation, message)
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

// CheckSeqNum checks the most recent sequence number and compares it to the current one to see if the application needs to run
//export CheckSeqNum
func CheckSeqNum() error {
	extensionMrseq, environmentMrseq, err := sequence.GetMostRecentSequenceNumber()
	shouldRun := sequence.ShouldBeProcessed(extensionMrseq, environmentMrseq)
	if !shouldRun {
		return errorhelper.AddStackToError(fmt.Errorf("environment mrseq has already been processed by extension (environment mrseq : %v, extension mrseq : %v)\n", environmentMrseq, extensionMrseq))
	}
	err = sequence.SetExtensionMostRecentSequenceNumber(environmentMrseq)
	return err
}

//export GetSettings
func GetSettings() (ProtectedSettings, PublicSettings) {
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
	return protectedSettings, publicSettings
}

func main(){
}