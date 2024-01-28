// Set your publishable key: remember to change this to your live publishable key in production
// See your keys here: https://dashboard.stripe.com/apikeys
let stripePublicKey = document.querySelector('#id_stripe_public_key').textContent.trim().slice(1, -1);
let clientSecret = document.querySelector('#id_client_secret').textContent.trim().slice(1, -1);
const stripe = Stripe(stripePublicKey);
let elements = stripe.elements();
let style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
let card = elements.create('card', { style: style });
card.mount('#card-element');

// Deal with realtime validation errors on card element
card.addEventListener('change', function (event) {
    let errorDiv = document.getElementById('card-errors');
    if (event.error) {
        let html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submit
let form = document.getElementById('payment-form');
let submitButton = document.getElementById('submit-button');
let loadingOverlay = document.getElementById('loading-overlay');
let cardErrors = document.getElementById('card-errors');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true });
    submitButton.setAttribute('disabled', true);
    
    // Use jQuery only for the fadeToggle effect
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);
    
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            // Construct the error message as HTML
            let html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            cardErrors.innerHTML = html;
            
            // Use jQuery only for the fadeToggle effect
            $('#payment-form').fadeToggle(100);
            $('#loading-overlay').fadeToggle(100);
            
            card.update({ 'disabled': false });
            submitButton.removeAttribute('disabled');
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});