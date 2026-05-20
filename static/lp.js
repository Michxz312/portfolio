function analyzeSystem() {
    const a1 = parseFloat(document.getElementById("a1").value);
    const b1 = parseFloat(document.getElementById("b1").value);
    const c1 = parseFloat(document.getElementById("c1").value);
    const a2 = parseFloat(document.getElementById("a2").value);
    const b2 = parseFloat(document.getElementById("b2").value);
    const c2 = parseFloat(document.getElementById("c2").value);
    const resultDiv = document.getElementById("result");
    const det = a1 * b2 - a2 * b1;

    if (det !== 0) {
        const x = (c1 * b2 - c2 * b1) / det;
        const y = (a1 * c2 - a2 * c1) / det;

        resultDiv.className = "result unique";
        resultDiv.innerHTML = 
        `Unique Solution<br><br>
        x = ${x.toFixed(2)}<br>
        y = ${y.toFixed(2)}`;

    } else {
    const ratioA = a1 / a2;
    const ratioB = b1 / b2;
    const ratioC = c1 / c2;
        if (nearlyEqual(ratioA, ratioB) && nearlyEqual(ratioB, ratioC)) {
        resultDiv.className = "result infinite";
        resultDiv.innerHTML = `
            Infinitely Many Solutions<br><br>
            The equations represent the same line.
        `;
        } else {
            resultDiv.className = "result none";
            resultDiv.innerHTML = `
                No Solution<br><br>
                The lines are parallel and never intersect.
            `;
        }
    }
}

document.getElementById("analyze").addEventListener("click", () => {
    analyzeSystem();
});