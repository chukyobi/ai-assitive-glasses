package main.java.com.example.userservice.service;

import org.springframework.mail.SimpleMailMessage;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.mail.javamail.MimeMessageHelper;
import org.springframework.stereotype.Service;
import org.thymeleaf.TemplateEngine;
import org.thymeleaf.context.Context;

import jakarta.mail.MessagingException;
import jakarta.mail.internet.MimeMessage;

@Service
@RequiredArgsConstructor
public class EmailService {
    private final JavaMailSender mailSender;
    private final TemplateEngine templateEngine;
    
    public void sendVerificationEmail(String to, String name, String token) throws MessagingException {
        Context context = new Context();
        context.setVariable("name", name);
        context.setVariable("token", token);
        
        String htmlContent = templateEngine.process("verification-email", context);
        
        MimeMessage message = mailSender.createMimeMessage();
        MimeMessageHelper helper = new MimeMessageHelper(message, true);
        helper.setTo(to);
        helper.setSubject("Verify your email");
        helper.setText(htmlContent, true);
        
        mailSender.send(message);
    }
    
    public void sendPasswordResetEmail(String to, String token) throws MessagingException {
        Context context = new Context();
        context.setVariable("token", token);
        
        String htmlContent = templateEngine.process("password-reset-email", context);
        
        MimeMessage message = mailSender.createMimeMessage();
        MimeMessageHelper helper = new MimeMessageHelper(message, true);
        helper.setTo(to);
        helper.setSubject("Password Reset Request");
        helper.setText(htmlContent, true);
        
        mailSender.send(message);
    }
}