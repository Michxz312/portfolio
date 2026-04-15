console.log("loaded")

document.getElementById("result").addEventListener("click", async() => {
    console.log("clicked")

    const data = {
        employees_data: window.APP_DATA.employees,
        customers_data: window.APP_DATA.customers,
    }

    const res = await fetch("/scheduling/result", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    const result = await res.json();

    console.log("result from Flask:", result);

    localStorage.setItem("result", JSON.stringify(result));
    window.location.href = "/scheduling/result_page"
});