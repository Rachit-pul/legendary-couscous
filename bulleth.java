import java.util.*;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
//import java.applet.*;
public class bulleth extends JFrame implements KeyListener,Runnable{
  public int frameWidth = 500,frameHeight = 500,loc_x = 235,loc_y = 450,size_width=50,size_height=40,death=0,score=0,x=0,y=0;
  public int count=0,b1x=65,b1y=0,b2x=frameHeight,b2y=0,b3x=frameHeight%13,b3y=0,i;
	Thread t;
	Random r = new Random();
	public bulleth(){
		setBounds(0,0,frameWidth,frameHeight);
		setVisible(true);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		repaint();
		Thread t = new Thread(this);
		t.start(); 
		addKeyListener(this);
	}
	public void update(){
		if(death==0){
			score++;
			y = y + 10;
			if(b1y<=frameHeight+30){
				b1y+=10;
			}
			if(b1y>frameHeight||y>frameHeight){
				b1x = r.ints(1, (frameWidth + 1)).limit(1).findFirst().getAsInt();
				b1y=0;
				y=0;
				count++;
			}
			if(b2y<=frameHeight+30){
					b2y+=10;
				}
				if(b2y>frameHeight){
					b2x = r.ints(1, (frameWidth + 1)).limit(1).findFirst().getAsInt();
					b2y=0;
			}
			if(b3y<=frameHeight+30){
					b3y+=10;
				}
				if(b3y>frameHeight){
					b3x = r.ints(1, (frameWidth + 1)).limit(1).findFirst().getAsInt();
					b3y=0;
			}
		if((loc_x+size_width)>b1x && ((loc_x<(b1x)) && ((y>loc_y-10) && (y<(loc_y+size_height)))))
		{
			death=1;
		}
		if((loc_x+size_width)>b2x && ((loc_x<(b2x)) && ((y>loc_y-10) && (y<(loc_y+size_height)))))
		{
			death=1;
		}
		if((loc_x+size_width)>b3x && ((loc_x<(b3x)) && ((y>loc_y-10) && (y<(loc_y+size_height)))))
		{
			death=1;
		}
		}
	}
	public void paint(Graphics g){
		if(death==0){
			super.paint(g);
			g.setColor(Color.black);
			g.fillRect(0,0,500,500);
			g.setColor(Color.white);
			g.fillOval(r.nextInt(500),r.nextInt(500),5,5);
	      	g.fillOval(r.nextInt(500),r.nextInt(500),5,5);
	      	g.fillOval(r.nextInt(500),r.nextInt(500),14,6);
	      	g.fillOval(r.nextInt(500),r.nextInt(500),5,10);
	      	g.fillOval(r.nextInt(500),r.nextInt(500),5,5);
	      	g.fillOval(r.nextInt(500),r.nextInt(500),5,5);
	      	g.fillOval(r.nextInt(500),r.nextInt(500),14,6);
	      	g.fillOval(r.nextInt(500),r.nextInt(500),5,10);
	      	g.fillOval(r.nextInt(500),r.nextInt(500),5,5);
	      	g.fillOval(r.nextInt(500),r.nextInt(500),5,5);
	      	g.fillOval(r.nextInt(500),r.nextInt(500),14,6);
	      	g.fillOval(r.nextInt(500),r.nextInt(500),5,10);
			g.setColor(Color.orange);
	      	g.fillRect(loc_x,loc_y,size_width,size_height);
	      	g.fillRect(loc_x,(loc_y+size_height),15,20);
	      	g.fillRect((loc_x+size_width-15),(loc_y+size_height),15,20);	
	      	g.setColor(Color.red);
	      	g.drawRect(100,0,300,50);
	      	g.drawString("ENEMY SHIP ",215,50);
	      	g.fillRect(0,0,500,40);
	      	g.setColor(Color.green);
	      	g.fillOval(b1x,y,20,20);
	      	g.fillOval(b2x,y,20,20);
	      	g.fillOval(b3x,y,20,20);
		}
		else{
			g.setColor(Color.white);
			g.drawString("YOU DIED ",frameWidth/2,frameHeight/2-50);

		}
		g.setColor(Color.white);
		g.drawString("Score:",frameWidth/2+10,frameHeight/2+10);
		g.drawString(String.valueOf(score),frameWidth/2+100,frameHeight/2+10);
	}
	public void keyTyped(KeyEvent ke){
	}
	public void keyReleased(KeyEvent ke){
	}
	public void keyPressed(KeyEvent ke){
		int key_id = ke.getKeyCode();
		if(key_id==KeyEvent.VK_LEFT && (loc_x>0)){
			loc_x-=58;
		}
		if(key_id==KeyEvent.VK_RIGHT && (loc_x<(500-size_width))){
			loc_x+=58;
		}
		if(key_id==KeyEvent.VK_UP && (loc_y>0)){
			loc_y-=58;
		}
		if((key_id==KeyEvent.VK_DOWN) && (loc_y<(500-size_height))){
			loc_y+=58;
		}
		repaint();
	}
	public void run(){
		while(true){
			repaint();
			update();
			try{	
			Thread.sleep(100);
			}
			catch (InterruptedException e){
				System.out.println(e);
			}
		}
	}


	public static void main(String args[]){
		new bulleth();
	}
}