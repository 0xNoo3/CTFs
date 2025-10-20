FROM openjdk:21-jdk-slim

WORKDIR /app

# Copy challenge files
COPY license.key .
COPY application.jar .

# Expose port
EXPOSE 8080

# Run the application
CMD ["java", "-javaagent:application.jar=-pwd pcc2025", "-jar", "application.jar"]