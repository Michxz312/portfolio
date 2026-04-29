const internationalCount = students.filter(s => s.international == 1).length;
const domesticCount = students.length - internationalCount;

const female = students.filter(s => s.gender == 1).length;
const male = students.length - female;

new Chart(document.getElementById('international_chart'), {
    type: 'pie',
    data: {
        labels: ['International', 'Domestic'],
        datasets: [{
            data: [internationalCount, domesticCount]
        }]
    }
})

new Chart(document.getElementById('gender_chart'), {
    type: 'pie',
    data: {
        labels: ['Female', 'Male'],
        datasets: [{
            data: [female, male]
        }]
    }
})