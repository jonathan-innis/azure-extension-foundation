package main

import "C"
import (
	"github.com/Azure/azure-extension-foundation/internal/status"
	"github.com/Azure/azure-extension-foundation/sequence"
	"github.com/Azure/azure-extension-foundation/errorhelper"
	"github.com/Azure/azure-extension-foundation/settings"
	"github.com/Azure/azure-extension-foundation/logger"
	"encoding/json"
	"fmt"
	"os"
	"path/filepath"
)

type ExtensionStatus string

const (
	statusTransitioning ExtensionStatus = "transitioning"
	statusError         ExtensionStatus = "error"
	statusSuccess       ExtensionStatus = "success"
)

type Settings map[string]interface{}
type PublicSettings interface{}
type ProtectedSettings interface{}

func (status ExtensionStatus) String() string {
	return string(status)
}

// ReportTransitioning reports the extension status as "transitioning"
//export ReportTransitioning
func ReportTransitioning(operation string, message string) *C.char {
	_, environmentMrseq, err := sequence.GetMostRecentSequenceNumber()
	if err != nil {
		err = errorhelper.AddStackToError(fmt.Errorf("unable to get sequence number : %v", err))
		return C.CString(ConvertErrorToString(err))
	}
	err = status.ReportStatus(environmentMrseq, statusTransitioning.String(), operation, message)
	return C.CString(ConvertErrorToString(err))
}

// ReportError reports the extension status as "error"
//export ReportError
func ReportError(operation string, message string) *C.char {
	_, environmentMrseq, err := sequence.GetMostRecentSequenceNumber()
	if err != nil {
		err = errorhelper.AddStackToError(fmt.Errorf("unable to get sequence number : %v", err))
		return C.CString(ConvertErrorToString(err))
	}
	err = status.ReportStatus(environmentMrseq, statusError.String(), operation, message)
	return C.CString(ConvertErrorToString(err))
}

// ReportSuccess reports the extension status as "success"
//export ReportSuccess
func ReportSuccess(operation string, message string) *C.char {
	_, environmentMrseq, err := sequence.GetMostRecentSequenceNumber()
	if err != nil {
		err = errorhelper.AddStackToError(fmt.Errorf("unable to get sequence number : %v", err))
		return C.CString(ConvertErrorToString(err))
	}
	err = status.ReportStatus(environmentMrseq, statusSuccess.String(), operation, message)
	return C.CString(ConvertErrorToString(err))
}

// CheckSeqNum checks the most recent sequence number and compares it to the current one to see if the application needs to run
//export CheckSeqNum
func CheckSeqNum() bool {
	extensionMrseq, environmentMrseq, _ := sequence.GetMostRecentSequenceNumber()
	shouldRun := sequence.ShouldBeProcessed(extensionMrseq, environmentMrseq)
	if !shouldRun {
		errorhelper.AddStackToError(fmt.Errorf("environment mrseq has already been processed by extension (environment mrseq : %v, extension mrseq : %v)\n", environmentMrseq, extensionMrseq))
		return false
	}
	sequence.SetExtensionMostRecentSequenceNumber(environmentMrseq)
	return true
}

//export GetSettings
func GetSettings() *C.char {
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
	settings := map[string]interface{}{"protectedSettings": protectedSettings, "publicSettings": publicSettings}
	return C.CString(ConvertSettingsToString(settings))
}

//export LogInfo
func LogInfo(message string){
	dir, err := filepath.Abs(filepath.Dir(os.Args[0])) // Get the current path of the main.go file
	if err != nil {
		errorhelper.AddStackToError(fmt.Errorf("unable to get path of the current file: %v", err))
		return
	}
	log := logger.NewLogger(dir, "file.log")
	log.Output(message)
}

//export LogWarning
func LogWarning(message string){
	dir, err := filepath.Abs(filepath.Dir(os.Args[0])) // Get the current path of the main.go file
	if err != nil {
		errorhelper.AddStackToError(fmt.Errorf("unable to get path of the current file: %v", err))
		return
	}
	log := logger.NewLogger(dir, "file.log")
	log.Output(message)
}

//export LogError
func LogError(message string){
	dir, err := filepath.Abs(filepath.Dir(os.Args[0])) // Get the current path of the main.go file
	if err != nil {
		errorhelper.AddStackToError(fmt.Errorf("unable to get path of the current file: %v", err))
		return
	}
	log := logger.NewLogger(dir, "file.log")
	log.Output(message)
}

func ConvertSettingsToString(settings Settings) string {
	jsonString, err := json.Marshal(settings)
	if err != nil {
		errorhelper.AddStackToError(fmt.Errorf("unable to convert settings into a json string: %v", err))
	}
	return string(jsonString)
}

func ConvertErrorToString(msg error) string{
	jsonString, err := json.Marshal(msg)
	if err != nil {
		errorhelper.AddStackToError(fmt.Errorf("unable to convert the error object into a json string: %v", err))
	}
	return string(jsonString)
}

func main(){}