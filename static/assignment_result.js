document.addEventListener("DOMContentLoaded", () => {
    const result = JSON.parse(localStorage.getItem("result"));

    preferences_count = [0,0,0,0]
    for (let i = 0; i < result.length; i++) {
        for (let j = 0; j < 4; j++) {
            if (result[i][j] > 0) {
                preferences_count[j] += 1
            }
        }
    }
    console.log(preferences_count)
    createStudentsPreference(preferences_count)
})

function createStudentsPreference(preferences_count) {
    const canvas = document.getElementById("studentPref").getContext("2d")
    const data = [{
        label: 'Student Preferences',
        data: preferences_count
    }]
    const chart = new Chart(canvas, {
        type: 'bar',
        data: {
            labels: ['1st', '2nd', '3rd', '4th'],
            datasets: data
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    })

}