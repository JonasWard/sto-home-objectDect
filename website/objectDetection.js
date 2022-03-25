let objectDetector;

async function detect() {
  if (!objectDetector) {
    objectDetector = await tflite.ObjectDetector.create(
      "https://storage.googleapis.com/tfhub-lite-models/tensorflow/lite-model/ssd_mobilenet_v1/1/metadata/2.tflite",
      { maxResults: 1 }
    );
  }
  const start = Date.now();
  const result = objectDetector.detect(document.querySelector("img"));
  const boundingBox = result[0].boundingBox;
  const clazz = result[0].classes[0];
  const strResult = `Bounding box: [${boundingBox.originX}, ${
    boundingBox.originY
  }, ${boundingBox.width}, ${boundingBox.height}]. Class: ${
    clazz.className
  }. Latency: ${Date.now() - start} ms`;
  document.querySelector(".result").textContent = strResult;
}

document.querySelector(".btn").addEventListener("click", () => {
  detect();
});