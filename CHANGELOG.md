# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

## v.0.0.2

- Wrap the contract optimisation in the `ContractOptimiser` class. 
- Add memray as a dev tool. 
- Improve memory efficiency of the `find_optimum` method on the `ContractOptimiser` 
class.
- Add memoization for the `find_optimum` method by caching the intermediate solutions.