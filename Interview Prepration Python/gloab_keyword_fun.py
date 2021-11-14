class Human:
    def __init__(self,ds,dn):
        self.data_analyst =dn;
        self.data_scientist =ds;
    def do_work(self):
        if self.data_analyst == "Analyse the data":
            print(self.data_analyst,"Get the insights from the data");
        elif self.data_scientist == "Take data decisions":
            print(self.data_scientist,"He Take Data Driven Decisions");
ob =Human("Analyse the data","abc")
ob.do_work()
class ComplexNumber:
    def __init__(self,r =0,i=0):
        self.real =r;
        self.imag =i;
    def get_data(self):
        print(f'{self.real}+{self.imag}j')
    def get_info(self):
        print("here real defines real_number");
        print("here image defines the imaginary number");

hi =ComplexNumber(2,3);
