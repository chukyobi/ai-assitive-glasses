package main.java.com.example.speechtotext;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;

@RestController
public class SpeechToTextController {

    @Autowired
    private SpeechToTextService speechToTextService;

    @PostMapping("/transcribe")
    public String transcribe(@RequestParam("file") MultipartFile file) throws IOException {
        // Save the file to a temporary location
        String filePath = "temp.wav"; // Replace with a more robust solution
        file.transferTo(new java.io.File(filePath));

        // Transcribe the audio
        String transcript = speechToTextService.transcribeAudio(filePath);

        // Delete the temporary file
        new java.io.File(filePath).delete();

        return transcript;
    }
}
