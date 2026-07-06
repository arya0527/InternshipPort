const API_URL = "http://127.0.0.1:5000";

export const uploadResume = async (
  file
) => {

  const formData = new FormData();

  formData.append(
    "resume",
    file
  );

  const response = await fetch(
    `${API_URL}/upload_resume`,
    {
      method: "POST",
      body: formData
    }
  );

  return response.json();
};