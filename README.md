# remotestorage-oauth-python

This tool allows to obtain an OAuth access token from a remoteStorage server.

## Usage

Configure `settings.py` with the authorization URL, the client ID, and the
required scopes.

Example:

```python
ENDPOINT = 'https://5apps.com/rs/oauth/cyroxx'
CLIENT = 'Vault'
SCOPES = ['vault:rw']
```

Run the server by `python server.py` and access the server in your browser.
By default, this is `localhost:5000`. You will automatically be redirected to
the configured OAuth authorization endpoint. At the end of the OAuth workflow,
you will find the access token included as the hash of the callback URI.

## Known Limitations

* The access token is only given in the callback URI and printed on the console.
  It would be nice to transform the logic into a library so that third-party
  applications can programatically authorize against a remoteStorage.
  Example: https://github.com/jcoglan/remotestorage-oauth
* Missing [WebFinger](http://hueniverse.com/2009/08/introducing-webfinger/) support.


## License

(The MIT License)

Copyright (c) 2013 Matthias Jacob

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the 'Software'), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

