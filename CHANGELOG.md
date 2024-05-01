# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.2.0] - 2024-05-01

### Changed

- Manage non-text values errors when parsings fields from a Line
- Fix bug on parsing document from string
- Refactor SinliCode:
  - replace Enum with dataclass
  - each encoded type has now its own class that inherits from EncodedField
  - when parsing lines, the field is saved as an EncodedField instead of its
      raw value
  - we can compare and set values with meaningful and autocompletable names,
      like `ORDERSOURCE.CLIENT` instead of `"C"`
- Fix bug on Document.to_readable(). Now, the result is a complete new document
    that doesn't reference to the original. This is important because readable
    fields can't be converted back nor serialized to sinli strings.

## [1.1.5] - 2024-04-10

### Added

- Parsing and building  SINLI messages (email) subject lines

## [1.1.4] - 2023-07-12

### Fixed

- Autopopulate the field FORMAT of long identification line and short and long id line TYPE fields. They were missed in 1.1.3

### Added

- Add source distribution in gitlab ci

## [1.1.3] - 2023-06-27

### Fixed

- Price and tax data types in LibrosDoc.Book. They are t.FLOAT now

### Added

- Document attributes doctype_code and version_code
- Autopopulate the identification lines fields that we can derive from their parent Document
- Example usage in the README

## [1.1.2] - 2023-05-22

### Changed

- Extend python requirements down to 3.7

## [1.1.1] - 2023-05-03

### Added

- A Changelog! :)

### Fixed

- Document parsing. It was broken by initializing all lines in 08f64a0a

## [1.1.0] - 2023-04-13

### Added

- Initialize lists and documents so that once created, all fields exist and can be accessed even if empty

### Fixed

- Pad differently strings ("A   ") and numbers ("001")
- List type hint

