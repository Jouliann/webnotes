function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

function deletedatadias(diasId) {
  fetch("/delete-data", {
    method: "POST",
    body: JSON.stringify({ diasId: diasId }),
  }).then((_res) => {
    window.location.href = "/dias";
  });
}
