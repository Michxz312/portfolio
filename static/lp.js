const a1 = parseFloat(document.getElementById("a1").value);
const b1 = parseFloat(document.getElementById("b1").value);
const c1 = parseFloat(document.getElementById("c1").value);
const a2 = parseFloat(document.getElementById("a2").value);
const b2 = parseFloat(document.getElementById("b2").value);
const c2 = parseFloat(document.getElementById("c2").value);
const a3 = parseFloat(document.getElementById("a3").value);
const b3 = parseFloat(document.getElementById("b3").value);
const c3 = parseFloat(document.getElementById("c3").value);

function analyzeSystem() {
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

function nearlyEqual(a, b, epsilon = 1e-10) {
    return Math.abs(a - b) < epsilon;
}

function drawGraph() {
    let data = [
        createLine(a1,b1,c1,"Line 1"),
        createLine(a2,b2,c2,"Line 2"),
        createLine(a3,b3,c3,"Line 3")
    ];
}

function createLine(a,b,c, name) {
    let x = []
    let y = []
    for (let xi=-10; xi<=10; xi+=0.1) {
        x.push(x1);
        if (Math.abs(b) >= 1e-10) {
            y.push((c- a*xi)/b);
        } else {
            y.push(null);
        }
    }
    return {
        x:x,
        y:y,
        mode:'lines',
        name:name
    }
}
document.getElementById("analyze").addEventListener("click", () => {
    analyzeSystem();
    drawGraph();
});