const internationalCount = students.filter(s => s.international == 1).length;
const domesticCount = students.length - internationalCount;

new Chart(document.getElementById('international_chart'), {
    type: 'pie',
    data: {
        labels: ['International', 'Domestic'],
        datasets: [{
            data: [internationalCount, domesticCount]
        }]
    }
})