package main

import "C"
import "github.com/Azure/azure-extension-foundation/internal/status"

type ExtensionStatus string

const (
	statusTransitioning ExtensionStatus = "transitioning"
	statusError         ExtensionStatus = "error"
	statusSuccess       ExtensionStatus = "success"
)

func (status ExtensionStatus) String() string {
	return string(status)
}

// ReportTransitioning reports the extension status as "transitioning"
//export ReportTransitioning
func ReportTransitioning(sequenceNumber int, operation string, message string) error {
	return status.ReportStatus(sequenceNumber, statusTransitioning.String(), operation, message)
}

// ReportError reports the extension status as "error"
//export ReportError
func ReportError(sequenceNumber int, operation string, message string) error {
	return status.ReportStatus(sequenceNumber, statusError.String(), operation, message)
}

// ReportError reports the extension status as "success"
//export ReportSuccess
func ReportSuccess(sequenceNumber int, operation string, message string) error {
	return status.ReportStatus(sequenceNumber, statusSuccess.String(), operation, message)
}

func main(){
}