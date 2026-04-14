const {
  renderStudent,
  renderSubjects,
  renderClassStudents,
} = require("../app");

describe("Frontend Render Test", () => {
  beforeEach(() => {
    document.body.innerHTML = `
      <div id="studentInfo"></div>

      <div id="subjectSection" style="display:none;">
        <table><tbody id="subjectTable"></tbody></table>
      </div>

      <div id="classSection" style="display:none;">
        <table><tbody id="classTable"></tbody></table>
      </div>

      <p id="error"></p>
    `;
  });

  test("render student info correctly", () => {
    const student = { id: 1, name: "A", class: "10A1" };

    renderStudent(student);

    const content = document.getElementById("studentInfo").innerHTML;

    expect(content).toContain("A");
    expect(content).toContain("10A1");
  });

  test("render subjects table correctly", () => {
    const subjects = [
      { id: 1, name: "Math" },
      { id: 2, name: "Physics" },
    ];

    renderSubjects(subjects);

    const rows = document.querySelectorAll("#subjectTable tr");

    expect(rows.length).toBe(2);
    expect(rows[0].textContent).toContain("Math");
  });

  test("render class students correctly", () => {
    const classmates = [
      { id: 1, name: "A", class: "10A1" },
      { id: 2, name: "B", class: "10A1" },
    ];

    renderClassStudents(classmates);

    const rows = document.querySelectorAll("#classTable tr");

    expect(rows.length).toBe(2);
    expect(rows[0].textContent).toContain("A");
  });

  test("handle empty data safely", () => {
    renderSubjects([]);
    renderClassStudents([]);

    const subjectRows = document.querySelectorAll("#subjectTable tr");
    const classRows = document.querySelectorAll("#classTable tr");

    expect(subjectRows.length).toBe(0);
    expect(classRows.length).toBe(0);
  });
});
