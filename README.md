# VAX QR Reader

A quick tool that allows you to decode the CA vaccine QR codes as given out at `https://myvaccinerecord.cdph.ca.gov`. Turns out is basically just a JWE with a weird encoding scheme in the actual QR code. Code is explained with comments if you want to do more with the script.

## Running
No dependencies, just run this with:

```
python3 main.py
```

The script expects a URI read from the QR code given of the form `shc:/{:digit:}*` to be passed through standard in.
