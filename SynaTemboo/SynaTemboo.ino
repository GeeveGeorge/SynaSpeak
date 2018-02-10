
#include <SPI.h>
#include <WiFi.h>
#include <WiFiClient.h>
#include <Temboo.h>
#include "TembooAccount.h" // Contains Temboo account information

WiFiClient client;

#define LED RED_LED
#define LED2 GREEN_LED
#define LED3 YELLOW_LED


int readValue = 0;   //value that is read from analogRead() function
int emailSent = 0;   //used to ensure email doesn't get sent more than once
int textSent = 0;    //used to ensure text doesn't get sent more than once
int dataLogged = 0;  //used to ensure data doesn't get logged more than once

//Synaspeak Variables
char ch;
String carr;
int i = 0;
int state = 0;


void setup() {
  Serial.begin(9600);
  pinMode(24, INPUT);      //sets the pin the sensor is connected to as an INPUT. 
  connectToInternet();    //connects to the internet
  Serial.println("Setup complete.\n");
  pinMode(LED, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);     

}

void loop() {


  if(Serial.available()>0){
          ch = Serial.read();
          carr += ch;
          Serial.println(ch);
          i++;
          if (i==2)
          {
              Serial.println("Array :" + carr);
              i = 0;
              if(carr == "EA")
              {
                  Serial.println("Emergency Alert!");
                  sendEmail();
                  sendSMS();
                  //logData();
              }
              else if(carr == "TN")
              {
                  if(state == 1)
                  {
                    Serial.println("Turning Off LED!");
                    digitalWrite(LED, LOW);
                    digitalWrite(LED2, LOW);
                    digitalWrite(LED3, LOW);
                    state = 0;
                  }
                  else if(state == 0)
                  {
                      Serial.println("Turn on LED!");
                      digitalWrite(LED, HIGH);
                      digitalWrite(LED2, HIGH);
                      digitalWrite(LED3, HIGH);
                      state = 1;
                  }
              }
              
              carr = ""; 
              
          }
               
  }
  
    delay(300);
}

void connectToInternet(){
    int wifiStatus = WL_IDLE_STATUS;

  // Determine if the WiFi Shield is present.
  Serial.print("\n\nShield:");
  if (WiFi.status() == WL_NO_SHIELD) {
    Serial.println("FAIL");

    // If there's no WiFi shield, stop here.
    while(true);
  }

  Serial.println("OK");

  // Try to connect to the local WiFi network.
  while(wifiStatus != WL_CONNECTED) {
    Serial.print("WiFi:");
    wifiStatus = WiFi.begin(WIFI_SSID, WPA_PASSWORD);

    if (wifiStatus == WL_CONNECTED) {
      Serial.println("OK");
    } else {
      Serial.println("FAIL");
    }
    delay(5000);
  }
}

void sendSMS(){
  Serial.println("Running SendSMS");

    TembooChoreo SendSMSChoreo(client);

    // Invoke the Temboo client
    SendSMSChoreo.begin();

    // Set Temboo account credentials
    SendSMSChoreo.setAccountName(TEMBOO_ACCOUNT);
    SendSMSChoreo.setAppKeyName(TEMBOO_APP_KEY_NAME);
    SendSMSChoreo.setAppKey(TEMBOO_APP_KEY);

    // Set profile to use for execution
    SendSMSChoreo.setProfile("XXXXXXX");

    // Set Choreo inputs
    String BodyValue = "I have an emergency!";
    SendSMSChoreo.addInput("Body", BodyValue);

    // Identify the Choreo to run
    SendSMSChoreo.setChoreo("/Library/Twilio/SMSMessages/SendSMS");

    // Run the Choreo; when results are available, print them to serial
    SendSMSChoreo.run();

    while(SendSMSChoreo.available()) {
      char c = SendSMSChoreo.read();
      Serial.print(c);
    }
    SendSMSChoreo.close();
    
    textSent = 1;
}


void sendEmail(){
  Serial.println("Running SendEmail");

    TembooChoreo SendEmailChoreo(client);

    // Invoke the Temboo client
    SendEmailChoreo.begin();

    // Set Temboo account credentials
    SendEmailChoreo.setAccountName(TEMBOO_ACCOUNT);
    SendEmailChoreo.setAppKeyName(TEMBOO_APP_KEY_NAME);
    SendEmailChoreo.setAppKey(TEMBOO_APP_KEY);

    // Set Choreo inputs
    String MessageBodyValue = "Emergency Alert!";
    SendEmailChoreo.addInput("MessageBody", MessageBodyValue);
    String SubjectValue = "WARNING!";
    SendEmailChoreo.addInput("Subject", SubjectValue);
    String PasswordValue = "XXXXXXX";
    SendEmailChoreo.addInput("Password", PasswordValue);
    String UsernameValue = "XXXXXXX";
    SendEmailChoreo.addInput("Username", UsernameValue);
    String FromAddressValue = "XXXXXXX";
    SendEmailChoreo.addInput("FromAddress", FromAddressValue);
    String ToAddressValue = "XXXXXXX";
    SendEmailChoreo.addInput("ToAddress", ToAddressValue);

    // Identify the Choreo to run
    SendEmailChoreo.setChoreo("/Library/Google/Gmail/SendEmail");

    // Run the Choreo; when results are available, print them to serial
    SendEmailChoreo.run();

    while(SendEmailChoreo.available()) {
      char c = SendEmailChoreo.read();
      Serial.print(c);
    }
    SendEmailChoreo.close();
  
  emailSent = 1;
}
  
