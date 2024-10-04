document.getElementById('generate-btn').addEventListener('click', function() {
    const name = document.getElementById('name').value;
    const github = document.getElementById('github').value;
    const facebook = document.getElementById('facebook').value;

    if (name && github && facebook) {
        // Make a POST request to the Flask backend
        fetch('/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name: name, github: github, facebook: facebook }),
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('output').innerHTML = `<p>${data.trollText}</p>`;
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('output').innerHTML = '<p>Error generating troll text!</p>';
        });
    } else {
        document.getElementById('output').innerHTML = '<p>Please fill in all fields!</p>';
    }
});
