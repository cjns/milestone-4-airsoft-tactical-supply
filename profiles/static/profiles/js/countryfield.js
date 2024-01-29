let countrySelected = document.querySelector('#id_default_country').value;
if (!countrySelected) {
    document.querySelector('#id_default_country').style.color = '#aab7c4';
}

document.querySelector('#id_default_country').addEventListener('change', function() {
    countrySelected = this.value;
    if (!countrySelected) {
        this.style.color = '#aab7c4';
    } else {
        this.style.color = '#000';
    }
});