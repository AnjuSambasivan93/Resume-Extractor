import {useResumeStore} from "../store/resumeStore"


function ResumeUpload() {
    const files = useResumeStore((state) => state.files)
    const setFiles = useResumeStore((state) => state.setFiles)
    return (
        <div className="resume-upload">
            <h2>Upload Resume</h2>

            <input
                type="file"
                accept=".pdf"
                multiple
                onChange={(event) => {
                    const selectedFiles = event.target.files
                    if (selectedFiles) {
                        setFiles(Array.from(selectedFiles));
                    }
                }}
                />
                <p>{files.length} file(s) selected</p>
        </div>
    )
}
export default ResumeUpload;