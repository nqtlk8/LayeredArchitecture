async function getStudentInfo() {
  const studentId = document.getElementById("studentId").value;
  const errorEl = document.getElementById("error");
  const subjectSection = document.getElementById("subjectSection");
  const classSection = document.getElementById("classSection");

  errorEl.textContent = "";
  subjectSection.style.display = "none";
  classSection.style.display = "none";

  if (!studentId) {
    errorEl.textContent = "Vui lòng nhập ID";
    return;
  }
  try {
    const response = await fetch(`http://localhost:8000/student/${studentId}`);
    if (!response.ok) {
      errorEl.textContent = "Không tìm thấy sinh viên";
      return;
    }
    const data = await response.json();
    if (!data.student) {
      errorEl.textContent = "Dữ liệu không hợp lệ";
      return;
    }
    renderStudent(data.student);
    renderSubjects(data.subjects || []);
    renderClassStudents(data.classmates || []);
    subjectSection.style.display = "block";
    classSection.style.display = "block";
  } catch (error) {
    console.error(error);
    errorEl.textContent = "Lỗi server";
  }
}

function renderStudent(student) {
  document.getElementById("studentInfo").innerHTML = `
    <h2>Thông tin sinh viên</h2>
    <p>ID: ${student.id}</p>
    <p>Name: ${student.name}</p>
    <p>Class: ${student.class}</p>
  `;
}

function renderSubjects(subjects) {
  const table = document.getElementById("subjectTable");
  table.innerHTML = "";

  subjects.forEach((sub) => {
    const row = document.createElement("tr");
    row.innerHTML = `
      <td>${sub.id}</td>
      <td>${sub.name}</td>
    `;
    table.appendChild(row);
  });
}

function renderClassStudents(list) {
  const table = document.getElementById("classTable");
  table.innerHTML = "";
  list.forEach((stu) => {
    const row = document.createElement("tr");
    row.innerHTML = `
      <td>${stu.id}</td>
      <td>${stu.name}</td>
      <td>${stu.class}</td>
    `;
    table.appendChild(row);
  });
}

// export để test
if (typeof module !== "undefined") {
  module.exports = {
    renderStudent,
    renderSubjects,
    renderClassStudents,
  };
}
