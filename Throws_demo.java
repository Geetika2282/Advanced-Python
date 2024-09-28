import java.io.File;
import java.io.IOException;

public class Throws_demo {
    public static void checkFile(String path) throws IOException{
        File f = new File(path);
        if(!f.exists())
            throw new IOException("File not present (throws)");
    }
    public static void main(String[] args) {
        try{
            checkFile("abc.txt");
        }
        catch (IOException io){
            io.printStackTrace();
        }

        System.out.println("After exception");
    }
}