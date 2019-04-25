// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT license.

package errorwrapping

import (
	"fmt"
	"github.com/pkg/errors"
	"testing"
)

func ErrorWithStack(stackDepth int, err error) error {
	if stackDepth == 0 {
		if err != nil {
			return errors.New(err.Error())
		} else {
			return errors.WithStack(fmt.Errorf("Reached the bottom of the error call stack"))
		}
	} else {
		return ErrorWithStack(stackDepth-1, err)
	}
}

func ErrorWithWrap(stackDepth int, err error) error {
	if stackDepth == 0 {
		if err != nil {
			return err
		} else {
			return fmt.Errorf("Reached the bottom of the error call stack")
		}
	} else {
		return errors.Wrap(ErrorWithWrap(stackDepth-1, err), fmt.Sprintf("stackDepth: %d\n", stackDepth))
	}
}

func ErrorWithoutStackOrWrap(stackDepth int, err error) error {
	if stackDepth == 0 {
		if err != nil {
			return err
		} else {
			return fmt.Errorf("Reached the bottom of the error call stack")
		}
	} else {
		return ErrorWithoutStackOrWrap(stackDepth-1, err)
	}
}

func TestErrorsWrap(t *testing.T) {
	err1 := ErrorWithStack(5, fmt.Errorf("misc error"))
	//err2 := ErrorWithWrap(5, fmt.Errorf("misc error"))
	err3 := ErrorWithoutStackOrWrap(5, fmt.Errorf("misc error"))

	t.Logf("the error stack trace is %+v", err1)
	//t.Logf("the error stack trace is %s, %+v", err2, err2)
	t.Logf("the error stack trace is %+v", err3)
}
