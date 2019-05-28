package logger

import (
	"os"
	"github.com/go-kit/kit/log"
	// "github.com/Azure/azure-extension-foundation/settings"
	"io"
	golog "log"
	"path"
)

type HandlerEnvironment struct {
	Version            float64 `json:"version"`
	Name               string  `json:"name"`
	HandlerEnvironment struct {
		HeartbeatFile string `json:"heartbeatFile"`
		StatusFolder  string `json:"statusFolder"`
		ConfigFolder  string `json:"configFolder"`
		LogFolder     string `json:"logFolder"`
	}
}

// ExtensionLogger for all the extension related events
type ExtensionLogger struct {
	logger      log.Logger
	logFilePath string
}

// create a new ExtensionLogger
func NewLogger(logPath, ExtensionHandlerLogFileName string) ExtensionLogger {
	// he, err := settings.GetHandlerEnvironment()
	// LOGDIR := he.HandlerEnvironment.LogFolder
	LOGDIR := "logs"
	if err := os.MkdirAll(LOGDIR, 0644); err != nil {
		golog.Printf("ERROR: Cannot create log folder %s: %v \r\n", LOGDIR, err)
	}

	extensionLogPath := path.Join(logPath, path.Join(LOGDIR, ExtensionHandlerLogFileName))
	golog.Printf("Logging in file %s: in directory %s: .\r\n", ExtensionHandlerLogFileName, logPath)

	fileHandle, err := os.OpenFile(extensionLogPath, os.O_CREATE|os.O_APPEND|os.O_WRONLY, 0644)

	if err != nil {
		golog.Fatalf("ERROR: Cannot open log file: %v \r\n", err)
	}

	fileLogger := log.With(
		log.With(
			log.NewSyncLogger(
				log.NewLogfmtLogger(
					io.MultiWriter(
						os.Stdout,
						os.Stderr,
						fileHandle))),
			"time", log.DefaultTimestamp))
	lg := ExtensionLogger{fileLogger, extensionLogPath}

	lg.Event("ExtensionLogPath: " + extensionLogPath)

	return lg
}

func (lg ExtensionLogger) With(key string, value string) {
	lg.logger = log.With(lg.logger, key, value)
}

func (lg ExtensionLogger) Output(output string) {
	lg.logger.Log(output)
}

func (lg ExtensionLogger) Event(event string) {
	lg.logger.Log(event)
}

func (lg ExtensionLogger) EventError(event string, error error) {
	lg.logger.Log(event, error)
}

func (lg ExtensionLogger) CustomLog(keyvals ...interface{}) {
	lg.logger.Log(keyvals)
}