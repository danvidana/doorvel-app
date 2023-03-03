# doorvel-app

doorvel-app is a Python API for dealing with CRUD operations of a postal codes database

## Development Plan

### 1st stage: MVP
1. Build GET endpoint -- DONE
1.1 ?Currently using JsonResponse. Need to find out how to use DRF to send only JSON, default sends whole HTML response -- Going to use normal Response class from DRF
2. Create MySQL instance and database schema -- DONE
3. Save postal codes (PCs) on MySQL database
3.1 ?Create script to add PCs from CSV to MySQL database
4. Create models for PCs
5. Connect Django with MySQL
6. Retrieve PC from GET Request

### 2nd stage: POST Method to add new PCs
### 3rd stage: PUT Method to update existing PCs



## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)