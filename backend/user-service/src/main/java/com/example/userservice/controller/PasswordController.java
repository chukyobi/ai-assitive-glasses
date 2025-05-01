package main.java.com.example.userservice.controller;

import com.example.userservice.dto.PasswordResetRequest;
import com.example.userservice.service.PasswordResetService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/auth/password")
@RequiredArgsConstructor
public class PasswordController {
    private final PasswordResetService passwordResetService;
    
    @PostMapping("/reset-request")
    public void requestPasswordReset(@RequestParam String email) {
        // Implementation to send password reset email
    }
    
    @PostMapping("/reset")
    public void resetPassword(@RequestBody PasswordResetRequest request) {
        // Implementation to reset password
    }
}