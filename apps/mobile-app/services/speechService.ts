// app/services/speechService.ts
import apiClient from './apiClient';

export async function transcribeAudio(audioBase64: string) {
  const response = await apiClient.post('/speech-to-text/transcribe', {
    audio: audioBase64,
  });
  return response.data;
}
