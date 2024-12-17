package main

import (
	"flag"
	"fmt"
	"io"
	"log/slog"
	"os"
	"plugin"

	"github.com/bazelbuild/rules_go/go/runfiles"
)

var (
	flagDay   = flag.Int("day", 0, "Day number to run")
	flagInput = flag.String("input", "puzzle", "Input file to use")
)

func lookupPartFn(plug *plugin.Plugin, dayNum int, partNum int) (func(io.Reader) (string, error), error) {
	fnName := fmt.Sprintf("Day%02d_P%d", dayNum, partNum)
	fnSym, err := plug.Lookup(fnName)
	if err != nil {
		return nil, fmt.Errorf("while looking up impl for day %d part %d: %w", dayNum, partNum, err)
	}
	if fn, ok := fnSym.(func(io.Reader) (string, error)); ok {
		return fn, nil
	} else {
		return nil, fmt.Errorf("func %q is of unexpected type %T", fnName, fn)
	}
}

func run() error {
	r, err := runfiles.New()
	if err != nil {
		return fmt.Errorf("failed to init runfiles: %w", err)
	}
	r = r.WithSourceRepo(runfiles.CurrentRepository())

	pluginLoc, err := r.Rlocation("_main/go/day/day_/day.dylib")
	if err != nil {
		return fmt.Errorf("can't find plugin in runfiles: %w", err)
	}
	plug, err := plugin.Open(pluginLoc)
	if err != nil {
		return fmt.Errorf("can't load plugin: %w", err)
	}

	inputName := fmt.Sprintf("_main/input/day%02d_%s.txt", *flagDay, *flagInput)
	input, err := r.Open(inputName)
	if err != nil {
		return fmt.Errorf("can't open input file %q: %w", inputName, err)
	}
	if part1, err := lookupPartFn(plug, *flagDay, 1); err != nil {
		slog.Warn("Skipping part 1 due to lookup failure", slog.Any("err", err))
	} else {
		if ans, err := part1(input); err != nil {
			slog.Error("Part 1 failure", slog.Any("err", err))
		} else {
			slog.Info("Part 1", slog.String("answer", ans))
		}
	}
	input.Close()

	input, err = r.Open(inputName)
	if err != nil {
		return fmt.Errorf("can't open input file %q: %w", inputName, err)
	}
	if part2, err := lookupPartFn(plug, *flagDay, 2); err != nil {
		slog.Warn("Skipping part 2 due to lookup failure", slog.Any("err", err))
	} else {
		if ans, err := part2(input); err != nil {
			slog.Error("Part 2 failure", slog.Any("err", err))
		} else {
			slog.Info("Part 2", slog.String("answer", ans))
		}
	}
	input.Close()

	return nil
}

func main() {
	flag.Parse()
	if err := run(); err != nil {
		slog.Error("Exiting due to error", slog.Any("err", err))
		os.Exit(1)
	}
}
