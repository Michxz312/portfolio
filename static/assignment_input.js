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

const female = students.filter(s => s.gender == 1).length;
const male = students.length - female;

new Chart(document.getElementById('gender_chart'), {
    type: 'pie',
    data: {
        labels: ['Female', 'Male'],
        datasets: [{
            data: [female, male]
        }]
    }
})

const rankCounts = {
    1: {},
    2: {},
    3: {},
    4: {}
};

students.forEach(s => {
    const p = s.preference.split(",").map(Number);
    p.forEach((course, rank) => {
        rankCounts[rank+1][course] = (rankCounts[rank+1][course] || 0) + 1;
    })
});

const courses_label = courses.map(c => c.id);
const datasets = courses_label.map(c => ({
    label: c,
    data: [1,2,3,4].map(r =>
        rankCounts[r][c] || 0
    )
}));

new Chart(document.getElementById('preference_chart'), {
    type: 'bar',
    data: {
        labels: ['1st', '2nd', '3rd', '4th'],
        datasets: datasets
    },
    options: {
        indexAxis: 'y',
        scales: {
            x: { stacked: true },
            y: { stacked: true }
        },
        plugins: {
            tooltip: {
                callbacks: {
                    label: function(tooltipItem) {
                        const dataset = tooltipItem.dataset;
                        const courseId = dataset.label;
                        const count = tooltipItem.raw;

                        return 'Course ID: '+ courseId + ', Count: ' + count;
                    }
                }
            }
        }
    },
})


document.getElementById("result").addEventListener("click", async() => {

    const data = {
        student_data: students,
        course_data: courses,
    }

    const res = await fetch("/assignment/result", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })

    const result = await res.json()

    localStorage.setItem("result", JSON.stringify(result));
    window.location.href = "/assignment/result_page"
})