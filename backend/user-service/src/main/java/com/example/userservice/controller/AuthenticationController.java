package com.example.userservice.controller;

import com.example.speechtotext.SpeechToTextService;
import com.example.userservice.dto.AuthenticationRequest;
import com.example.userservice.dto.AuthenticationResponse;
import com.example.userservice.dto.RegisterRequest;
import com.example.userservice.service.AuthenticationService;
import com.example.userservice.service.VerificationService;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;

@RestController
@RequestMapping("/api/v1/auth")
@RequiredArgsConstructor
public class AuthenticationController {

    private static final String BLUETOOTH_ADDRESS = "00:11:22:33:44:55"; // Replace with the actual Bluetooth address
    private static final int BLUETOOTH_PORT = 1;

    @Autowired
    private SpeechToTextService speechToTextService;

    @Autowired
    private VerificationService verificationService;

    private void sendTextToBluetooth(String text) {
        try {
            // Code to connect to Bluetooth device and send text
            // This is a placeholder and needs to be implemented using the bluecove library
            System.out.println("Sending text to Bluetooth: " + text);

            // Example using bluecove (This is just a placeholder and might not work directly)
            // RemoteDevice device = RemoteDevice.getRemoteDevice(BLUETOOTH_ADDRESS);
            // UUID uuid = new UUID("94f39d297d6d437d973bfba39e49d4ee", false);
            // String connectionString = "btspp://" + device.getBluetoothAddress() + ":" + uuid;
            // StreamConnection streamConnection = Connector.open(connectionString);
            // OutputStream os = streamConnection.openOutputStream();
            // os.write(text.getBytes());
            // os.close();
            // streamConnection.close();

        } catch (Exception e) {
            System.err.println("Error sending text to Bluetooth: " + e.getMessage());
        }
    }

    @PostMapping("/transcribe")
    public String transcribe(@RequestParam("file") MultipartFile file) throws IOException {
        // Save the file to a temporary location
        String filePath = "temp.wav"; // Replace with a more robust solution
        try {
            file.transferTo(new java.io.File(filePath));
            // Transcribe the audio
            String transcript = speechToTextService.transcribeAudio(filePath);

            // Send the transcribed text to the Bluetooth device
            sendTextToBluetooth(transcript);

            // Delete the temporary file
            new java.io.File(filePath).delete();

            return transcript;
        } catch (Exception e) {
            return "Error transcribing audio: " + e.getMessage();
        }
    }

    private final AuthenticationService authenticationService;

    @PostMapping("/register")
    public ResponseEntity<AuthenticationResponse> register(
            @RequestBody RegisterRequest request
    ) {
        return ResponseEntity.ok(authenticationService.register(request));
    }

    @PostMapping("/authenticate")
    public ResponseEntity<AuthenticationResponse> authenticate(
            @RequestBody AuthenticationRequest request
    ) {
        return ResponseEntity.ok(authenticationService.authenticate(request));
    }

    @GetMapping("/verify-email")
    public ResponseEntity<String> verifyEmail(@RequestParam("token") String token) {
        try {
            authenticationService.verifyUser(token);
            return ResponseEntity.ok("Email verified successfully!");
        } catch (Exception e) {
            return ResponseEntity.badRequest().body("Error verifying email: " + e.getMessage());
        }
    }
}
