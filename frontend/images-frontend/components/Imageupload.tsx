'use client'
import { useState } from 'react';

export default function Home() {
    const [image, setImage] = useState(null);
    const [processedImage, setProcessedImage] = useState(null);

    const handleImageChange = (e:any) => {
        setImage(e.target.files[0]);
    };

    const handleSubmit = async (e:any) => {
        e.preventDefault();
        const formData = new FormData();
        if(!image) {
          alert("image is null")
          return
        }
        formData.append('image', image);

        const res = await fetch('http://127.0.0.1:8000/api/process-image/', {
            method: 'POST',
            body: formData
        });
        if (res.ok) {
          const blob = await res.blob();
          console.log(blob)
          const url:any = URL.createObjectURL(blob);
          setProcessedImage(url);
      } else {
          console.error('Failed to process image');
      }
    };

    return (
        <div>
            <h1>Upload Image</h1>
            <form onSubmit={handleSubmit}>
                <input type="file" onChange={handleImageChange} />
                <button type="submit">Submit</button>
            </form>
            {processedImage && (
                <div>
                    <h2>Processed Image</h2>
                    <img src={`data:image/jpeg;base64,${processedImage}`} alt="Processed" />
                </div>
            )}
        </div>
    );
}
