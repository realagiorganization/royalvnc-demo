#!/usr/bin/env python3
import argparse
import os
import sys
from steps import STEP_DEFINITIONS


def load_features(features_dir):
    features = []
    for name in sorted(os.listdir(features_dir)):
        if not name.endswith('.feature'):
            continue
        path = os.path.join(features_dir, name)
        with open(path, 'r', encoding='utf-8') as handle:
            features.append((path, handle.read().splitlines()))
    return features


def parse_feature(lines):
    current_feature = None
    current_scenario = None
    data = []
    for line in lines:
        raw = line.strip()
        if not raw or raw.startswith('#'):
            continue
        if raw.startswith('Feature:'):
            current_feature = raw[len('Feature:'):].strip()
            continue
        if raw.startswith('Scenario:'):
            if current_scenario:
                data.append(current_scenario)
            current_scenario = {
                'name': raw[len('Scenario:'):].strip(),
                'steps': [],
                'feature': current_feature,
            }
            continue
        for prefix in ('Given', 'When', 'Then', 'And'):
            if raw.startswith(prefix + ' '):
                step_text = raw[len(prefix) + 1:]
                if current_scenario is None:
                    raise ValueError('Step found outside of a Scenario')
                current_scenario['steps'].append(step_text)
                break
    if current_scenario:
        data.append(current_scenario)
    return data


def find_step(step_text):
    for pattern, handler in STEP_DEFINITIONS:
        match = pattern.match(step_text)
        if match:
            return handler, match.groups()
    return None, None


def run(features_dir, show_steps=True):
    failures = 0
    scenarios_run = 0
    for path, lines in load_features(features_dir):
        scenarios = parse_feature(lines)
        for scenario in scenarios:
            scenarios_run += 1
            ctx = {}
            if show_steps:
                print(f"Feature: {scenario['feature']}")
                print(f"  Scenario: {scenario['name']}")
            for step_text in scenario['steps']:
                handler, groups = find_step(step_text)
                if handler is None:
                    failures += 1
                    if show_steps:
                        print(f"    [FAIL] {step_text}")
                    continue
                handler(ctx, *groups)
                if show_steps:
                    print(f"    [PASS] {step_text}")
            if show_steps:
                print("")
    return failures, scenarios_run


def main():
    parser = argparse.ArgumentParser(description='Run lightweight BDD checks.')
    parser.add_argument('--features', default=os.path.join('bdd', 'features'))
    parser.add_argument('--format', default='plain', choices=['plain', 'quiet'])
    args = parser.parse_args()

    show_steps = args.format == 'plain'
    failures, scenarios_run = run(args.features, show_steps=show_steps)

    if scenarios_run == 0:
        print('No scenarios found.')
        return 1
    if failures:
        print(f"BDD failures: {failures}")
        return 1
    print(f"BDD scenarios passed: {scenarios_run}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
