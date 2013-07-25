import os
import urllib
from flask import Flask, url_for, request, render_template, redirect

from settings import ENDPOINT, CLIENT, SCOPES

DEBUG = os.environ.get('DEBUG', False)

app = Flask(__name__)


@app.route("/")
def index():
    """Redirect to the service provider."""

    params = {
        'client_id': CLIENT,
        'redirect_uri': url_for('receive', _external=True),
        'response_type': 'token',
        'scope': ' '.join(SCOPES)
    }

    encparams = urllib.urlencode(params)
    sep = '?' if not '?' in ENDPOINT else '&'

    full_uri = '%s%s%s' % (ENDPOINT, sep, encparams)

    return redirect(full_uri)


@app.route('/receive')
def receive():
    target = url_for('rxpost')
    return render_template('receive.html', target=target)


@app.route('/rxpost', methods=['POST'])
def rxpost():
    """Handle OAuth response."""

    # TODO we could do something useful here with the token
    print request.form.get('access_token')
    print request.form.get('error')
    return ''

if __name__ == "__main__":
    app.run(debug=DEBUG)
