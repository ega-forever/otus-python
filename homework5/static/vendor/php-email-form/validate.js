(function () {

  const form = document.getElementById('email-form');

  form.addEventListener('submit', function(event) {
      event.preventDefault();

      let thisForm = this;

      let action = thisForm.getAttribute('action');

      if( ! action ) {
        displayError(thisForm, 'The form action property is not set!')
        return;
      }
      thisForm.querySelector('.loading').classList.add('d-block');
      thisForm.querySelector('.error-message').classList.remove('d-block');
      thisForm.querySelector('.sent-message').classList.remove('d-block');

      let formData = new FormData( thisForm );

      php_email_form_submit(thisForm, action, formData).catch((error) => {
      displayError(thisForm, error);
      });
    });

  async function php_email_form_submit(thisForm, action, formData) {
    const response = await fetch(action, {
      method: 'POST',
      body: formData,
      headers: {'X-Requested-With': 'XMLHttpRequest'}
    });

    if( !response.ok ) {
        throw new Error(`${response.status} ${response.statusText} ${response.url}`);
    }

    const data = await response.json();

    thisForm.querySelector('.loading').classList.remove('d-block');
    if (data.sent == 1) {
      thisForm.querySelector('.sent-message').classList.add('d-block');
      thisForm.reset();
    } else {
      throw new Error(data ? data : 'Form submission failed and no error message returned from: ' + action);
    }
  }

  function displayError(thisForm, error) {
    thisForm.querySelector('.loading').classList.remove('d-block');
    thisForm.querySelector('.error-message').innerHTML = error;
    thisForm.querySelector('.error-message').classList.add('d-block');
  }

})();
