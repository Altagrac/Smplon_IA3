// // Sélectionne le formulaire et la zone d'affichage des résultats
// const form = document.querySelector('form');
// const resultDiv = document.querySelector('#result');

// // Ajoute un écouteur d'événements au formulaire
// form.addEventListener('submit', event => {
//   // Empêche le comportement par défaut du formulaire (rechargement de la page)
//       event.preventDefault();

//       // Récupère la valeur de l'entrée utilisateur
//       const countryInput = document.querySelector('#country-input').value;

//         // Envoie une requête à l'API REST de Rest Countries pour récupérer les informations sur le pays
//         fetch(`https://restcountries.com/v3.1/name/${countryInput}`)
//           .then(response => response.json()) // Convertit la réponse en JSON
//           .then(data => {
//             // Récupère les informations sur le pays à partir de la réponse JSON
//             const countryData = data[0];
//             const capital = countryData.capital[0];
//             const currency = countryData.currency[0];

//             // Affiche les informations sur le pays dans la zone d'affichage des résultats
//             resultDiv.textContent = `La capitale de ${countryInput} est ${capital} et la monnaie est ${currency}.`;
//           })
//           .catch(error => {
//             // Affiche un message d'erreur si la requête échoue
//             console.error(error);
//             resultDiv.textContent = `Impossible de trouver des informations sur le pays ${countryInput}.`;
//           });
//       });

// Sélectionne le formulaire et la zone d'affichage des résultats
const form = document.querySelector('form');
const resultDiv = document.querySelector('#result');
const countryNameElement = document.querySelector('.country-name');
const countryCapitalElement = document.querySelector('.country-capital');
const countryRegionElement = document.querySelector('.country-region');
const countrySubregionElement = document.querySelector('.country-subregion');

// Ajoute un écouteur d'événements au formulaire
form.addEventListener('submit', event => {
  event.preventDefault();  // Empêche le comportement par défaut du formulaire (rechargement de la page)

  // Récupère la valeur de l'entrée utilisateur
  const countryInput = document.querySelector('#country-input').value;

   // Envoie une requête à l'API REST de Rest Countries pour récupérer les informations sur le pays
  fetch(`https://restcountries.com/v3.1/name/${countryInput}`)
    .then(response => response.json())
    .then(data => {
      const countryData = data[0];
      const capital = countryData.capital[0];
      const region = countryData.region;
      const subregion = countryData.subregion;
      countryNameElement.textContent = countryInput;
      countryCapitalElement.textContent = capital;
      countryRegionElement.textContent = region;
      countrySubregionElement.textContent = subregion;
      resultDiv.style.display = 'block';
    })
    .catch(error => {
      console.error(error);
      resultDiv.textContent = `Impossible de trouver des informations sur le pays ${countryInput}.`;
      resultDiv.style.display = 'none';
    });
});
