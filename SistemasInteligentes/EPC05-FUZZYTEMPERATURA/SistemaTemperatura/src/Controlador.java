/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/**
 *
 * @author allen
 */
 
  import java.io.File;
  import java.nio.file.Files;
import java.util.ArrayList;
import java.util.List;
  import java.util.logging.Level;
  import java.util.logging.Logger;
  import net.sourceforge.jFuzzyLogic.FIS;
   
  public class Controlador {
      
      private FIS fis;
   
      public Controlador() {
          iniciaInferencia();
      }
      
       private void iniciaInferencia() {
          try {
              File arquivoFis = new File(Controlador.class.getResource("Caldeira.FLC").toURI());
              String conteudoArquivoFis = new String(Files.readAllBytes(arquivoFis.toPath()));
              fis = FIS.createFromString(conteudoArquivoFis, true);
              System.out.println("Instancia de inferencias carregada com sucesso");
          } catch (Exception ex) {
              Logger.getLogger(Controlador.class.getName()).log(Level.SEVERE, "Erro ao abrir o arquivo", ex);
          }
      }
      
      public double calculaInferencia(double temperatura, double volume){
          this.fis.setVariable("Temperatura", temperatura);
          this.fis.setVariable("Volume", volume);
          this.fis.evaluate();
          conjuntosFuzzyAtivados();
          double pressao = this.fis.getVariable("Pressao").getLatestDefuzzifiedValue();
          return pressao;
      }
      
      public static void main(String[] args) {
          Controlador c = new Controlador();
          int[] temperaturas = {965,920,1050,843,1122};
          double[] volumes = {11,7.6,6.3,8.6,5.2};
          for(int i = 0; i < temperaturas.length; i++) 
            System.out.println(c.calculaInferencia(temperaturas[i], volumes[i]));
      }

    private void conjuntosFuzzyAtivados() {
        System.out.println(this.fis.getVariable("Temperatura"));
        System.out.println(this.fis.getVariable("Volume"));
        System.out.println(this.fis.getVariable("Pressao"));
    }
  }
