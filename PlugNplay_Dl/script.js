function detectLanguage() {
  var text = document.getElementById('text').value;

  axios.post('/', {
      text: text
  })
  .then(response => {
      document.getElementById('result').innerHTML = 'La langue du texte est : ' + response.data.language;
  })
  .catch(error => {
      console.error('Erreur:', error);
  });
}
