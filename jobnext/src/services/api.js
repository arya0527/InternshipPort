export const API_BASE_URL = "https://internshipport-production.up.railway.app";

export const uploadResume = async (
  file
) => {

  const formData = new FormData();

  formData.append(
    "resume",
    file
  );

  const response = await fetch(
    `${API_BASE_URL}/upload_resume`,
    {
      method: "POST",
      body: formData
    }
  );

  return response.json();
};