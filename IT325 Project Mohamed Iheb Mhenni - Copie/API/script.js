function getQuranEdition() {
    const editionInput = document.getElementById('quranEdition');
    const edition = editionInput.value;

    fetch(`http://localhost:3000/quran-edition?edition=${edition}`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Error: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            const resultDiv = document.getElementById('resultQuranEdition');
            resultDiv.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
        })
        .catch(error => {
            console.error(`Error: ${error.message}`);
            const resultDiv = document.getElementById('resultQuranEdition');
            resultDiv.innerHTML = `<p>Error: ${error.message}</p>`;
        });
}

function getQuranPage() {
    const pageInput = document.getElementById('page');
    const editionInput = document.getElementById('pageEdition');

    const page = pageInput.value;
    const edition = editionInput.value;

    fetch(`http://localhost:3000/quran-page?page=${page}&edition=${edition}`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Error: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            const resultDiv = document.getElementById('resultQuranPage');
            resultDiv.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
        })
        .catch(error => {
            console.error(`Error: ${error.message}`);
            const resultDiv = document.getElementById('resultQuranPage');
            resultDiv.innerHTML = `<p>Error: ${error.message}</p>`;
        });
}

function getSajdaAyahs() {
    const editionInput = document.getElementById('sajdaEdition');
    const edition = editionInput.value;

    fetch(`http://localhost:3000/sajda-ayahs?edition=${edition}`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Error: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            const resultDiv = document.getElementById('resultSajdaAyahs');
            resultDiv.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
        })
        .catch(error => {
            console.error(`Error: ${error.message}`);
            const resultDiv = document.getElementById('resultSajdaAyahs');
            resultDiv.innerHTML = `<p>Error: ${error.message}</p>`;
        });
}

function getAsmaAlHusna() {
    const numbersInput = document.getElementById('asmaNumbers');
    const numbers = numbersInput.value;

    fetch(`http://localhost:3000/asma-al-husna?numbers=${numbers}`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Error: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            const resultDiv = document.getElementById('resultAsmaAlHusna');
            resultDiv.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
        })
        .catch(error => {
            console.error(`Error: ${error.message}`);
            const resultDiv = document.getElementById('resultAsmaAlHusna');
            resultDiv.innerHTML = `<p>Error: ${error.message}</p>`;
        });
}
function getPrayerTimes() {
    const cityInput = document.getElementById('prayerCity');
    const countryInput = document.getElementById('prayerCountry');

    const city = cityInput.value;
    const country = countryInput.value;

    fetch(`http://localhost:3000/prayer-times?city=${city}&country=${country}`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Error: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            const resultDiv = document.getElementById('resultPrayerTimes');
            resultDiv.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
        })
        .catch(error => {
            console.error(`Error: ${error.message}`);
            const resultDiv = document.getElementById('resultPrayerTimes');
            resultDiv.innerHTML = `<p>Error: ${error.message}</p>`;
        });
}

function getCalendarByCity() {
    const yearInput = document.getElementById('calendarYear');
    const monthInput = document.getElementById('calendarMonth');
    const cityInput = document.getElementById('calendarCity');
    const countryInput = document.getElementById('calendarCountry');

    const year = yearInput.value;
    const month = monthInput.value;
    const city = cityInput.value;
    const country = countryInput.value;

    fetch(`http://localhost:3000/calendar-by-city?year=${year}&month=${month}&city=${city}&country=${country}`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Error: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            const resultDiv = document.getElementById('resultCalendarByCity');
            resultDiv.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
        })
        .catch(error => {
            console.error(`Error: ${error.message}`);
            const resultDiv = document.getElementById('resultCalendarByCity');
            resultDiv.innerHTML = `<p>Error: ${error.message}</p>`;
        });
}