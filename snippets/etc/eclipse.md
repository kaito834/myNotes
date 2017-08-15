# Install on Windows
## Environments
- Windows 10 (64 bit)
- Eclipse
  * Version: Oxygen Release (4.7.0)
  * Build id: 20170620-1800
- JRE and JDK version 8 update 144 (1.8_144)

## Procedures
1. Install JRE and JDK
  - JRE: https://www.java.com/ja/download/windows-64bit.jsp
  - JDK: http://www.oracle.com/technetwork/java/javase/downloads/index.html
2. Download Eclipse packages
  - https://eclipse.org/downloads/eclipse-packages/
  - For this procedures, select "Eclipse IDE for Java EE Developers"
3. Expand the downloaded Eclipse packages
4. Launch 'eclipse.exe'

# Build sample Jersey/Jetty Web application
## Environments
- Windows 10 (64 bit)
- Eclipse
  * Version: Oxygen Release (4.7.0)
  * Build id: 20170620-1800
- JRE and JDK version 8 update 144 (1.8_144)
- Git for Windows 2.10.1
- Apache Maven 3.5.0

## Target application
- https://github.com/ralmodiel/jersey-jetty-executable-war-sample

## Procedures
1. Install Apache Maven based on the following documents
  - https://maven.apache.org/download.cgi
  - https://maven.apache.org/install.html
2. `git clone git@github.com:ralmodiel/jersey-jetty-executable-war-sample.git`
3. Launch Eclipse
4. Open [File] menu -> [Import...], and then launch import dialog Window
5. Select "Existing Maven Projects", and click "Next >" button
6. Browse cloned directory, select pom.xml at Projects area, and click "Finish" button
7. Launch Windows command prompt at cloned directory
8. `mvn clean package`
9. `java -DCONFIGPATH=.\sample.properties -jar .\target\jersey-jetty-executable-war-sample.war`
10. Launch Web browser, and access http://localhost:8383/sample/hello/there/json

# References
- Apache Maven
  * [Maven – Running Apache Maven](https://maven.apache.org/run.html)
  * [Maven – Password Encryption](https://maven.apache.org/guides/mini/guide-encryption.html)
- [JavaEE使い方メモ（基本＋環境構築） - Qiita](http://qiita.com/opengl-8080/items/aeda0d8bad42af3113bd) (in Japanese)
  * The following sections are helpful for me to understand Java EE
    + Java EE 7 に含まれている仕様の例
    + JSR とは
    + リファレンス実装とは
