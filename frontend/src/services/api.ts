export async function analyzeResumes(formData: FormData){
    const response = await fetch("http://127.0.0.1:8000/analyze/",{
        method: "POST",
        body: formData
    }
)
 return response.json()
}