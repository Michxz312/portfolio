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

document.getElementById("result").addEventListener("click", async() => {
    console.log("clicked")

    const data = {
        student_data: students,
        course_data: courses,
    }
    console.log(data)
    const res = await fetch("/assignment/result", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })

    const result = await res.json()

    console.log("result", result)

    localStorage.setItem("result", JSON.stringify(result));
    window.location.href = "/assignment/result_page"
})