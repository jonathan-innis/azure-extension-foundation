// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT license.

package settings

import "github.com/Azure/azure-extension-foundation/internal/settings"

// GetExtensionSettings reads the settings for the provided sequenceNumber and assigns the settings to the
// respective structure reference
func GetExtensionSettings(sequenceNumber int, publicSettings, protectedSettings interface{}) error {
	return settings.GetExtensionSettings(sequenceNumber, publicSettings, protectedSettings)
}