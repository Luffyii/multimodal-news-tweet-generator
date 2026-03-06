import { useState } from "react"

function App() {
  const [file, setFile] = useState(null)
  const [preview, setPreview] = useState(null)
  const [data, setData] = useState(null)
  const [loading, setLoading] = useState(false)

  const handleFile = (e) => {
    const f = e.target.files[0]
    setFile(f)
    setPreview(URL.createObjectURL(f))
  }

  const generateTweet = async () => {
    if (!file) {
      alert("Upload an image first")
      return
    }

    const formData = new FormData()
    formData.append("file", file)

    setLoading(true)

    const res = await fetch("http://127.0.0.1:8000/generate_tweet", {
      method: "POST",
      body: formData
    })

    const result = await res.json()

    setData(result)
    setLoading(false)
  }

  const copyTweet = () => {
    if (!data?.tweet) return
    navigator.clipboard.writeText(data.tweet)
    alert("Tweet copied to clipboard!")
  }

  return (
    <div className="min-h-screen bg-gradient-to-r from-slate-800 to-gray-500 flex justify-center items-start py-16">

      <div className="bg-black text-white w-full max-w-3xl rounded-xl shadow-xl p-10">

        {/* Header */}
        <h1 className="text-3xl font-bold text-center mb-2">
          📰 Multimodal News → Tweet Generator
        </h1>

        <p className="text-center text-gray-400 mb-8">
          Upload a news image and automatically generate a tweet using AI
        </p>

        {/* Image preview */}
        {preview && (
          <div className="flex justify-center mb-6">
            <img
              src={preview}
              className="rounded-lg max-h-40"
            />
          </div>
        )}

        {/* Upload */}
        <div className="flex items-center justify-center gap-4 mb-6">

          <input
            type="file"
            onChange={handleFile}
            className="text-sm"
          />

          <button
            onClick={generateTweet}
            className="bg-green-500 hover:bg-green-600 px-5 py-2 rounded-lg font-semibold"
          >
            Generate Tweet
          </button>

        </div>

        {loading && (
          <p className="text-center text-yellow-400 mb-6">
            Generating tweet with AI...
          </p>
        )}

        {/* Results */}
        {data && (
          <div className="space-y-6">

            <div className="bg-gray-900 p-6 rounded-xl">
              <h2 className="font-semibold text-lg mb-2">
                📰 Headline
              </h2>
              <p>{data.headline}</p>
            </div>

            <div className="bg-gray-900 p-6 rounded-xl">
              <h2 className="font-semibold text-lg mb-2">
                🖼 Image Caption
              </h2>
              <p>{data.caption}</p>
            </div>

            <div className="bg-gray-900 p-6 rounded-xl">
              <h2 className="font-semibold text-lg mb-2">
                🐦 Generated Tweet
              </h2>

              <p className="text-blue-400 mb-4">
                {data.tweet}
              </p>

              <button
                onClick={copyTweet}
                className="bg-blue-500 hover:bg-blue-600 px-4 py-2 rounded-lg"
              >
                Copy Tweet
              </button>

            </div>

          </div>
        )}

      </div>

    </div>
  )
}

export default App