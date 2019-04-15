# Parsemesan
This grate repository will unbrielievably parse your CSV string and
return a Python dictionary with headers and rows of data. You cheddar
believe I put some gouda tests in here.

All cheesiness aside, the goal of this project is to allow the parsing
of CSV files to stand alone as a separate service and remove the
burden from the frontend code of Datasmith and later Wordsmith. This
project will most likely expand to include other data formats.

## Getting Started

##### Installation
Python 3.6+ is required. From repo root, run `pip install -r requirements.txt`

##### Tests
From repo root, run `pytest`
From repo root, run `pylint parsemesan tests`

##### Coverage

From repo root, run `coverage run -m pytest && coverage html`

## Documentation

### API

**`parse_data`**

##### Params

 - **{str}**: `source_type` the type of data source (`arrays`, `csv`, `unicode`)
 - **{*}**: `input_data` CSV `{bytes}` or Python `{list}` or Python `{str}` (which is Unicode)

##### Return

 - **{dict}**: Python object with following spec:
     ```
    {
        "errors": [
            <dict>
        ]
        "result": {
            "headers": <list of {str}>
            "rows": <list of lists of {str}>
        }
    }
    ```

**`get_valid_formats`**

##### Params

 - No inputs required.

##### Return

 - **{dict}**: Python object with following spec:
     ```
    {
        "formats": <list of {str}>
    }
    ```


### Types and Errors

 - `byte_string`: a raw Python `bytes` array. Does not apply to `source_type='arrays'`. `EncodingError` raised if not valid.
 - `stream`: a Python object that reads the data sequentially. `FileTypeError` raised if not valid.
 - `data`: a Python dictionary with keys `headers` and `rows` (see below). `DataError` raised if not valid.

### Pipelines
Each pipeline combines a `parser` and at least one `validator`, as shown in the `pipelines/` directory.

#### Arrays
The `input_data` is a Python `{list}` of `{lists}` containing the rows of data.

1. Parse or reorganize the object into `data`.
2. Validate the `data`'s rows and headers as proper tabular.

`data` is returned as described above.

#### CSV
The `input_data` is a Python `{bytes}` object containing an encoded CSV table.

1. Detect `input_data` encoding using the `chardet` module.
2. Validate the `byte_string`'s encoding by calling the native `.decode(encoding)` function.
3. Convert it to a `stream` with the native `ioString` module.
4. Validate the `stream`'s file type by eliminating other common possibilities of files (`.html`, `.xml`).
5. Parse the stream into `data` using the native `csv` module.
6. Validate the `data`'s rows and headers as proper tabular.

`data` is returned as described above.

#### Unicode
The `input_data` is a Python `{str}` object (which is Unicode in Python 3) containing an encoded CSV table.

1. Convert the string to a `stream` with the native `ioString` module.
2. Validate the `stream`'s file type by eliminating other common possibilities of files (`.html`, `.xml`).
3. Parse the stream into `data` using the native `csv` module.
4. Validate the `data`'s rows and headers as proper tabular.

`data` is returned as described above.

