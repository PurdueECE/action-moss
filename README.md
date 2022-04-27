# MOSS Action
This action will run the [MOSS](https://theory.stanford.edu/~aiken/moss/) checker on the provided files.

# Usage
```yaml
- uses: PurdueECE/action-moss@main
  # MOSS system user ID
  # Required
  user_id: 123456
  # usage: file1 file2 file3 ... [-l language] [-d] [-b basefile1] ... [-b basefilen] [-m #] [-c "string"]
  # Required
  args: file1.py -l 'python'
```

# Testing
## Unit
Unit tests are in the `test-unit/` directory. They can be run with `pytest`.