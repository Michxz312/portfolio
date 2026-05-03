document.addEventListener("DOMContentLoaded", () => {
    const result = JSON.parse(localStorage.getItem("result"));
    const preferences_count = result.preferences_count
    const students_in_course = result.students_in_course
    const preference_assignment_count = result.preference_assignment_count

    createStudentsPreference(preference_assignment_count)
})

function createStudentsPreference(preference_assignment_count) {
    const canvas = document.getElementById("studentPref").getContext("2d")
    const data = [{
        label: 'Student Preferences',
        data: preference_assignment_count
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